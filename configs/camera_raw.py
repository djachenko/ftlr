from ftlr.xmp_types import Factory

__types = Factory.instance()


def calculate_optimal_exposure():
    """Вычисляет оптимальную экспозицию на основе статистики"""
    # Здесь можно добавить логику анализа гистограммы
    return 0.2

def calculate_optimal_contrast():
    """Вычисляет оптимальный контраст"""
    return 15

# Вычисляем значения
optimal_exposure = calculate_optimal_exposure()
optimal_contrast = calculate_optimal_contrast()

# Функция для разворачивания иерархического словаря
def __flatten_dict(d):
    result = []
    for key, value in d.items():
        if not isinstance(value, dict):
            result.append((key, *value))
            continue
        tuples = __flatten_dict(value)
        for path, *rest in tuples:
            result.append(("/".join([key, path]), *rest))
    return result

# Иерархическая структура, отражающая структуру XMP файла
__dict_mapping = {
    "x:xmpmeta": {
        "rdf:RDF": {
            "rdf:Description": {
                # Camera Raw Settings - основные параметры
                "@crs:Exposure2012": ("exposure", __types.real(), float),
                "@crs:Contrast2012": ("contrast", __types.integer(), int),
                "@crs:Highlights2012": ("highlights", __types.integer(), int),
                "@crs:Shadows2012": ("shadows", __types.integer(), int),
                "@crs:Whites2012": ("whites", __types.integer(), int),
                "@crs:Blacks2012": ("blacks", __types.integer(), int),
                "@crs:Clarity2012": ("clarity", __types.integer(), int),
                "@crs:Vibrance": ("vibrance", __types.integer(), int),
                "@crs:Saturation": ("saturation", __types.integer(), int),
                "@crs:Temperature": ("temperature", __types.integer(), int),
                "@crs:Tint": ("tint", __types.integer(), int),
                
                # Детализация
                "@crs:Sharpness": ("sharpness", __types.integer(), int),
                "@crs:LuminanceSmoothing": ("luminance-smoothing", __types.integer(), int),
                "@crs:ColorNoiseReduction": ("color-noise-reduction", __types.integer(), int),
                "@crs:VignetteAmount": ("vignette", __types.integer(), int),
                
                # Цветовые настройки
                "@crs:RedHue": ("red-hue", __types.integer(), int),
                "@crs:RedSaturation": ("red-saturation", __types.integer(), int),
                "@crs:GreenHue": ("green-hue", __types.integer(), int),
                "@crs:GreenSaturation": ("green-saturation", __types.integer(), int),
                "@crs:BlueHue": ("blue-hue", __types.integer(), int),
                "@crs:BlueSaturation": ("blue-saturation", __types.integer(), int),
                

            },
        },
    },
}

# Экспортируем готовый CONFIG
CONFIG = __flatten_dict(__dict_mapping) 