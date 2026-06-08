# Dev Utilities

Coleção de programas, scripts e ferramentas auxiliares desenvolvidos para automatizar tarefas, processar dados e apoiar projetos maiores.

Este repositório reúne pequenos utilitários criados durante o desenvolvimento de sistemas, permitindo reutilização e manutenção independente das aplicações principais.

---

## Estrutura

```text
.
│   conversor-csv-json.py
│
├── maps
│   │   gerar_coordenadas.py
│   │   gerar_mapa.c
│   │   mapa.html
│   │
│   └───data
│           lojas_com_coord.json
│           lojas_exemplo.json
│
└───tratamento-dados-ufs
        associar_ufs.py
        estados.json
        municipios.json
        municipios_com_estado.json
```

## Ferramentas
### Conversor CSV para JSON

Arquivo:

conversor-csv-json.py

Realiza a conversão de arquivos CSV para JSON, facilitando a integração de dados com aplicações web, APIs e sistemas desktop.

### Ferramentas de Mapas

Pasta:

```maps/```

Utilitários relacionados a geolocalização e visualização de dados em mapas.

```gerar_coordenadas.py```

Obtém ou associa coordenadas geográficas aos registros de entrada.

```gerar_mapa.c```

Gera um arquivo mapa.html para visualização geográfica em um mapa interativo.

## Tratamento de Dados de Estados e Municípios

Pasta:

```tratamento-dados-ufs/```

Scripts para enriquecimento e associação de dados geográficos brasileiros.

associar_ufs.py

Relaciona municípios aos respectivos estados utilizando códigos oficiais.

Arquivos de dados:
```
estados.json
municipios.json
municipios_com_estado.json
```

## Projetos que Utilizam Estas Ferramentas

As ferramentas deste repositório foram desenvolvidas para auxiliar a criação, manutenção e processamento de dados utilizados em outros projetos.

### Sistema Localizador Comercial

Projeto desktop desenvolvido em C e Qt para centralização e consulta de informações de lojas vinculadas à Casa do Militar.

Ferramentas utilizadas:

- Conversão de bases de dados CSV para JSON;
- Associação de municípios aos respectivos estados;
- Enriquecimento de dados geográficos com coordenadas;
- Geração e validação de mapas para visualização das informações.

O objetivo é manter os utilitários desacoplados do projeto principal, permitindo sua reutilização em outros sistemas e facilitando a manutenção das ferramentas de processamento de dados.
