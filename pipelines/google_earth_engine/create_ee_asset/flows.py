# -*- coding: utf-8 -*-
"""
Database  dumping flows for SEOP project
"""

from copy import deepcopy

from prefect.run_configs import KubernetesRun
from prefect.storage import GCS
from prefeitura_rio.pipelines_templates.dump_earth_engine.flows import (
    flow as dump_earth_engine_asset_flow,
)
from prefeitura_rio.pipelines_utils.prefect import set_default_parameters
from prefeitura_rio.pipelines_utils.state_handlers import (
    handler_initialize_sentry,
    handler_inject_bd_credentials,
)

from pipelines.constants import constants

seop_ee_flow = deepcopy(dump_earth_engine_asset_flow)
seop_ee_flow.name = "SEOP: Earth Engine - Criar asset"
seop_ee_flow.state_handlers = [handler_inject_bd_credentials, handler_initialize_sentry]

seop_ee_flow.storage = GCS(constants.GCS_FLOWS_BUCKET.value)
seop_ee_flow.run_config = KubernetesRun(
    image=constants.DOCKER_IMAGE.value,
    labels=[
        constants.RJ_SEOP_AGENT_LABEL.value,
    ],
)

seop_ee_default_parameters = {
    "project_id": "rj-seop",
    "query": "",
    "bd_project_mode": "prod",
    "billing_project_id": "rj-seop",
    "service_account": "earth-engine@rj-seop.iam.gserviceaccount.com",
    "vault_path_earth_engine_key": "seop_earth_engine_key",
    "gcs_asset_path": "gs://rj-seop/assets/",
    "ee_asset_path": "projects/rj-seop/assets/",
}
seop_ee_flow = set_default_parameters(seop_ee_flow, default_parameters=seop_ee_default_parameters)
