SELECT 
    SAFE_CAST(globalid AS STRING) id_global, # identificacao unica para cada entrada 
    SAFE_CAST(boletim AS STRING) id_boletim,
    SAFE_CAST(boletim_pe AS STRING) periodo_boletim, # periodo de cobertura do boletim
    SAFE_CAST(periodo AS STRING) periodo, # TODO: converter para ultimo mes de referencia
    SAFE_CAST(regiao_adm AS STRING) nome_regiao_administrativa,
    SAFE_CAST(REGEXP_REPLACE(LTRIM(codra ,'0'), r'.0$', '') AS STRING) id_regiao_administrativa,
    SAFE_CAST(area_plane AS STRING) id_area_planejamento,
    SAFE_CAST(bairro AS STRING) nome_bairro,
    SAFE_CAST(REGEXP_REPLACE(LTRIM(codbairro ,'0') , r'.0$', '') AS STRING) id_bairro,
    SAFE_CAST(acesso AS STRING) acesso_local,
    SAFE_CAST(tipo AS STRING) tipo_local,
    SAFE_CAST(obs AS STRING) observacao,
    SAFE_CAST(uc AS STRING) nome_unidade_conservacao,
    SAFE_CAST(area AS FLOAT64) area,
    SAFE_CAST(latitude AS FLOAT64) latitude,
    SAFE_CAST(longitude AS FLOAT64) longitude,
    SAFE_CAST(geometry AS STRING) geometria_wkt, 
    SAFE.ST_GEOGFROMTEXT(geometry) AS geometry, 
FROM rj-seop.conservacao_ambiental_monitor_verde_staging.alertas_desmatamento