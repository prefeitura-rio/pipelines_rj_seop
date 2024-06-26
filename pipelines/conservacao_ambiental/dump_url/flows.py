# -*- coding: utf-8 -*-
"""
Database  dumping flows for SEOP project
"""

from copy import deepcopy

from prefect.run_configs import KubernetesRun
from prefect.storage import GCS
from prefeitura_rio.pipelines_templates.dump_url.flows import dump_url_flow
from prefeitura_rio.pipelines_utils.prefect import set_default_parameters
from prefeitura_rio.pipelines_utils.state_handlers import (
    handler_initialize_sentry,
    handler_inject_bd_credentials,
)

from pipelines.conservacao_ambiental.dump_url.schedules import (
    gsheets_year_update_schedule,
)
from pipelines.constants import constants

seop_gsheets_flow = deepcopy(dump_url_flow)
seop_gsheets_flow.name = "SEOP: Concervacao Ambiental - Ingerir CSV do Google Drive"
seop_gsheets_flow.state_handlers = [handler_inject_bd_credentials, handler_initialize_sentry]

seop_gsheets_flow.storage = GCS(constants.GCS_FLOWS_BUCKET.value)
seop_gsheets_flow.run_config = KubernetesRun(
    image=constants.DOCKER_IMAGE.value,
    labels=[
        constants.RJ_SEOP_AGENT_LABEL.value,
    ],
)

seop_gsheets_default_parameters = {
    "dataset_id": "conservacao_ambiental_monitor_verde",
}
seop_gsheets_flow = set_default_parameters(
    seop_gsheets_flow, default_parameters=seop_gsheets_default_parameters
)

seop_gsheets_flow.schedule = gsheets_year_update_schedule
