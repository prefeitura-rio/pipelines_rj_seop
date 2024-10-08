# -*- coding: utf-8 -*-
# flake8: noqa: E501
"""
Schedules for the database dump pipeline
"""

from datetime import datetime, timedelta

import pytz
from prefect.schedules import Schedule
from prefeitura_rio.pipelines_utils.io import untuple_clocks as untuple
from prefeitura_rio.pipelines_utils.prefect import generate_dump_url_schedules

from pipelines.constants import constants

#####################################
#
# Monitor Verde Schedule
#
#####################################

gsheets_urls = {
    "alertas_desmatamento": {
        "dump_mode": "overwrite",
        "url": "https://drive.google.com/file/d/1Q5MbIStFAWzM1q9Vf82xzKBYAZHNt9l6/view?usp=share_link",
        "url_type": "google_drive",
        "materialize_after_dump": True,
        "dataset_id": "conservacao_ambiental_monitor_verde",
    },
    "licencas": {
        "dump_mode": "overwrite",
        "url": "https://drive.google.com/file/d/14GieP41HlKSgr5T9xifELOQr4G2acwNQ/view?usp=share_link",
        "url_type": "google_drive",
        "materialize_after_dump": True,
        "dataset_id": "urbanismo_geosislic_licenciamento",
    },
}

gsheets_clocks = generate_dump_url_schedules(
    interval=timedelta(days=365),
    start_date=datetime(2022, 11, 4, 20, 0, tzinfo=pytz.timezone("America/Sao_Paulo")),
    labels=[
        constants.RJ_SEOP_AGENT_LABEL.value,
    ],
    dataset_id="",
    table_parameters=gsheets_urls,
)

gsheets_year_update_schedule = Schedule(clocks=untuple(gsheets_clocks))
