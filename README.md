# Dev Utilities

Coleção de programas, scripts e ferramentas auxiliares desenvolvidos para automatizar tarefas, processar dados e apoiar projetos maiores.

Este repositório reúne pequenos utilitários criados durante o desenvolvimento de sistemas, permitindo reutilização e manutenção independente das aplicações principais.

---

## Estrutura

```text
.
│   README.md
│
├───comparativo
│   ├───versao 1
│   │       comparativo.c
│   │       total.txt
│   │       VerSeTem.txt
│   │
│   └───versao 2
│           comparativoV2.c
│           usuarios.txt
│
├───conversor
│       conversor-csv-json.py
│
├───criar login i-manager
│       GerarLoginI-Manager.c
│       logins.txt
│       nomes.txt
│
├───gerar senha
│       GenPasswordLOL.c
│       GenPasswordVava.c
│
├───maps
│   │   gerar_coordenadas.py
│   │   gerar_mapa.c
│   │   mapa.html
│   │
│   └───data
│           lojas_com_coord.json
│           lojas_exemplo.json
│
├───primários
│   │   base.c
│   │   ContadorCaracteres.c
│   │   DetectarTecla.c
│   │   entrada.txt
│   │   mouse.c
│   │   pixel.c
│   │
│   └───Correção do @
│           CorrecaoCVS.c
│           teste.c
│
└───tratamento-dados-ufs
    │   associar_ufs.py
    │
    └───data
            estados.json
            municipios.json
            municipios_com_estado.json
```

## Ferramentas

### Conversão e Tratamento de Dados

#### Conversor CSV para JSON

**Pasta** `conversor/`

Realiza a conversão de arquivos CSV para JSON, facilitando a integração de dados com aplicações web, APIs e sistemas desktop.

#### Tratamento de Dados de Estados e Municípios

**Pasta:** `tratamento-dados-ufs/`

Scripts utilizados para enriquecimento e organização de dados geográficos brasileiros.

**Principais recursos:**

* Associação de municípios aos respectivos estados;
* Utilização de códigos oficiais do IBGE;
* Geração de bases enriquecidas para consulta e processamento de dados.

---

### Geolocalização e Mapas

#### Ferramentas de Mapas

**Pasta:** `maps/`

Conjunto de utilitários para geolocalização e visualização de dados em mapas.

**Principais recursos:**

* Associação de coordenadas geográficas;
* Geração de arquivos para visualização cartográfica;
* Criação de mapas interativos em HTML.

---

### Comparação e Validação de Dados

#### Comparador de Registros

**Pasta:** `comparativo/`

Ferramenta desenvolvida para identificar divergências entre bases de dados e listas de usuários.

**Principais recursos:**

* Localização de registros existentes;
* Identificação de registros ausentes;
* Comparação entre diferentes bases de dados;
* Geração de relatórios para conferência.

---

### Gestão de Usuários

#### Gerador de Logins

**Pasta:** `criar login i-manager/`

Automatiza a criação de logins a partir de listas de nomes, reduzindo trabalho manual em processos de cadastro.

#### Geradores de Senha

**Pasta:** `gerar senha/`

Ferramentas para geração automatizada de senhas destinadas a diferentes cenários de utilização.

---

### Manipulação de Arquivos e Automação

#### Utilitários Diversos

**Pasta:** `primários/`

Coleção de programas experimentais e ferramentas auxiliares utilizadas em estudos, testes e automações.

**Inclui exemplos como:**

* Manipulação de arquivos texto;
* Contagem de caracteres;
* Detecção de teclas;
* Captura de informações do mouse;
* Leitura de pixels da tela;
* Tratamento e correção de arquivos CSV;
* Testes de entrada e saída de dados.

---

## Objetivo

Este repositório reúne ferramentas auxiliares criadas ao longo do desenvolvimento de diferentes projetos. Os programas são independentes entre si e têm como objetivo automatizar tarefas repetitivas, processar dados, validar informações e acelerar atividades de desenvolvimento.