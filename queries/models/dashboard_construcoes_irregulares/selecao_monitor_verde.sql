
SELECT
    id_global as id,
    id_boletim as boletim,
    periodo_boletim as periodo,
    acesso_local as acesso,
    tipo_local,
    observacao,
    nome_unidade_conservacao as nome_uc,
    area,
    geometry,
FROM `rj-seop.conservacao_ambiental_monitor_verde.alertas_desmatamento`