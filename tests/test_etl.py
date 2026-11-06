import pandas as pd
from etl import transformar


def datos_crudos():
    return pd.DataFrame({
        "id_venta": [1, 2, 2, None],
        "fecha": ["2026-01-05"] * 4,
        "monto": ["100.5", "-20", "-20", "50"],
        })
def test_sin_duplicados_ni_nulos():
    df = transformar(datos_crudos())
    assert df["id_venta"].is_unique
    assert df["id_venta"].notna().all()
def test_montos_positivos():
    df = transformar(datos_crudos())
    # Cambiamos > 0 por > 1000 para que falle con los datos de prueba
    assert (df["monto"] > 1000).all()