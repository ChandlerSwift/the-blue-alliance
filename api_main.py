#!/usr/bin/env python
import webapp2

import tba_config

from controllers.api_controller import ApiDeprecatedController, CsvTeamsAll
from controllers.api.api_district_controller import ApiDistrictListController, ApiDistrictEventsController, ApiDistrictRankingsController
from controllers.api.api_team_controller import ApiTeamController, ApiTeamEventsController, ApiTeamEventAwardsController, \
                                                ApiTeamEventMatchesController, ApiTeamMediaController, ApiTeamListController, \
                                                ApiTeamYearsParticipatedController, ApiTeamHistoryEventsController, ApiTeamHistoryAwardsController
from controllers.api.api_event_controller import ApiEventController, ApiEventTeamsController, \
                                                 ApiEventMatchesController, ApiEventStatsController, \
                                                 ApiEventRankingsController, ApiEventAwardsController, \
                                                 ApiEventDistrictPointsController, ApiEventListController
from controllers.api.api_match_controller import ApiMatchController
from controllers.api.api_trusted_controller import ApiTrustedEventAllianceSelectionsUpdate, ApiTrustedEventAwardsUpdate, \
                                                   ApiTrustedEventMatchesUpdate, ApiTrustedEventMatchesDelete, ApiTrustedEventRankingsUpdate, \
                                                   ApiTrustedEventTeamListUpdate, ApiTrustedAddMatchYoutubeVideo


app = webapp2.WSGIApplication([webapp2.Route(r'/api/v1/<:.*>',
                                             ApiDeprecatedController,
                                             methods=['GET']),
                               ('/api/csv/teams/all', CsvTeamsAll),
                               webapp2.Route(r'/api/v2/team/<team_key:>',
                                             ApiTeamController,
                                             methods=['GET']),
                               webapp2.Route(r'/api/v2/team/<team_key:>/events',
                                             ApiTeamEventsController,
                                             methods=['GET']),
                               webapp2.Route(r'/api/v2/team/<team_key:>/<year:([0-9]*)>/events',
                                             ApiTeamEventsController,
                                             methods=['GET']),
                               webapp2.Route(r'/api/v2/team/<team_key:>/event/<event_key:>/awards',
                                             ApiTeamEventAwardsController,
                                             methods=['GET']),
                               webapp2.Route(r'/api/v2/team/<team_key:>/event/<event_key:>/matches',
                                             ApiTeamEventMatchesController,
                                             methods=['GET']),
                               webapp2.Route(r'/api/v2/team/<team_key:>/media',
                                             ApiTeamMediaController,
                                             methods=['GET']),
                               webapp2.Route(r'/api/v2/team/<team_key:>/<year:([0-9]*)>/media',
                                             ApiTeamMediaController,
                                             methods=['GET']),
                               webapp2.Route(r'/api/v2/team/<team_key:>/history/events',
                                             ApiTeamHistoryEventsController,
                                             methods=['GET']),
                               webapp2.Route(r'/api/v2/team/<team_key:>/history/awards',
                                             ApiTeamHistoryAwardsController,
                                             methods=['GET']),
                               webapp2.Route(r'/api/v2/team/<team_key:>/years_participated',
                                             ApiTeamYearsParticipatedController,
                                             methods=['GET']),
                               webapp2.Route(r'/api/v2/teams/<page_num:([0-9]*)>',
                                             ApiTeamListController,
                                             methods=['GET']),
                               webapp2.Route(r'/api/v2/event/<event_key:>',
                                             ApiEventController,
                                             methods=['GET']),
                               webapp2.Route(r'/api/v2/event/<event_key:>/teams',
                                             ApiEventTeamsController,
                                             methods=['GET']),
                               webapp2.Route(r'/api/v2/event/<event_key:>/matches',
                                             ApiEventMatchesController,
                                             methods=['GET']),
                               webapp2.Route(r'/api/v2/event/<event_key:>/stats',
                                             ApiEventStatsController,
                                             methods=['GET']),
                               webapp2.Route(r'/api/v2/event/<event_key:>/rankings',
                                             ApiEventRankingsController,
                                             methods=['GET']),
                               webapp2.Route(r'/api/v2/event/<event_key:>/awards',
                                            ApiEventAwardsController,
                                            methods=['GET']),
                               webapp2.Route(r'/api/v2/event/<event_key:>/district_points',
                                            ApiEventDistrictPointsController,
                                            methods=['GET']),
                               webapp2.Route(r'/api/v2/events/<year:([0-9]*)>',
                                             ApiEventListController,
                                             methods=['GET']),
                               webapp2.Route(r'/api/v2/match/<match_key:>',
                                             ApiMatchController,
                                             methods=['GET']),
                               webapp2.Route(r'/api/v2/districts/<year:([0-9]*)>',
                                             ApiDistrictListController,
                                             methods=['GET']),
                               webapp2.Route(r'/api/v2/district/<district_abbrev:>/<year:([0-9]*)>/events',
                                             ApiDistrictEventsController,
                                             methods=['GET']),
                               webapp2.Route(r'/api/v2/district/<district_abbrev:>/<year:([0-9]*)>/rankings',
                                             ApiDistrictRankingsController,
                                             methods=['GET']),
                               webapp2.Route(r'/api/trusted/v1/event/<event_key:>/alliance_selections/update',
                                             ApiTrustedEventAllianceSelectionsUpdate,
                                             methods=['POST']),
                               webapp2.Route(r'/api/trusted/v1/event/<event_key:>/awards/update',
                                             ApiTrustedEventAwardsUpdate,
                                             methods=['POST']),
                               webapp2.Route(r'/api/trusted/v1/event/<event_key:>/matches/update',
                                             ApiTrustedEventMatchesUpdate,
                                             methods=['POST']),
                               webapp2.Route(r'/api/trusted/v1/event/<event_key:>/matches/delete',
                                             ApiTrustedEventMatchesDelete,
                                             methods=['POST']),
                               webapp2.Route(r'/api/trusted/v1/event/<event_key:>/rankings/update',
                                             ApiTrustedEventRankingsUpdate,
                                             methods=['POST']),
                               webapp2.Route(r'/api/trusted/v1/event/<event_key:>/team_list/update',
                                             ApiTrustedEventTeamListUpdate,
                                             methods=['POST']),
                               webapp2.Route(r'/api/trusted/v1/event/<event_key:>/match_videos/add',
                                             ApiTrustedAddMatchYoutubeVideo,
                                             methods=['POST']),
                               ], debug=tba_config.DEBUG)
