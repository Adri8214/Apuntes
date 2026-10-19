def resumir_importes(importes):
    if len(importes) == 0:
        return None

    total = sum(importes)

    return {
        "Total": total,
        "Media": total / len(importes),
        "Minimo": min(importes),
        "Máximo": max(importes)
    }

importes = [10, 20, 30, 40, 50]

resumen = resumir_importes(importes)

if importes is not None:
    print(resumen)