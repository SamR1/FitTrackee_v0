from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

import pandas

from ..activities.models import Activity


class UserActivitiesList(APIView):

    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):

        color = ['rgba(151,187,205,0.2)', 'rgba(247,70,74,0.2)', 'rgba(148,159,177,0.2)',
                 'rgba(70,191,189,0.2)', 'rgba(253,180,92,0.2)']
        color_border = ['blue', 'red', 'grey', 'green', 'yellow']
        activities_df = pandas.DataFrame([(activity.activity_date, activity.sport.label) for
                                          activity in Activity.objects.all().order_by('-activity_date').filter(
                                          user_id=request.user.id)[:10]], columns=['Date', 'Sport'])

        labels_sport = activities_df.Sport.unique()

        activities_data = []
        dataframe_dict = {elem: pandas.DataFrame for elem in labels_sport}

        i = 0
        for key in dataframe_dict.keys():
            dataframe_dict[key] = activities_df[:][activities_df.Sport == key]
            del dataframe_dict[key]['Sport']
            temp_dict = {
                'label': key,
                'backgroundColor': color[i],
                'borderColor': color_border[i],
                'borderWidth': 1,
                'data': [dataframe_dict[key]['Date'].count()]
            }
            activities_data.append(temp_dict)
            i += 1
            if i > 4:
                i = 0

        data = {
            "labels": labels_sport,
            "activities": activities_data
        }
        return Response(data)
