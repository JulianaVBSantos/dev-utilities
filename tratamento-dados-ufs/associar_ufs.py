import json

with open("estados.json", "r", encoding="utf-8-sig") as f:
    estados = json.load(f)

with open("municipios.json", "r", encoding="utf-8-sig") as f:
    municipios = json.load(f)

estados_por_codigo = {
    estado["codigo_uf"]: estado
    for estado in estados
}

for municipio in municipios:
    codigo_uf = municipio["codigo_uf"]

    estado = estados_por_codigo.get(codigo_uf)

    if estado:
        municipio["uf"] = estado["uf"]
        municipio["estado"] = estado["nome"]
        municipio["regiao"] = estado["regiao"]

with open(
    "municipios_com_estado.json",
    "w",
    encoding="utf-8"
) as f:
    json.dump(
        municipios,
        f,
        ensure_ascii=False,
        indent=4
    )

print(f"{len(municipios)} municípios processados com sucesso!")
print("Arquivo gerado: municipios_com_estado.json")