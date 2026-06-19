from ftlr.xmp_types import Factory

__types = Factory.instance()

# Функции для работы с EXIF данными
def validate_iso(value):
    """Проверяет корректность значения ISO"""
    return 50 <= value <= 25600

def validate_shutter_speed(value):
    """Проверяет корректность выдержки"""
    return 1/8000 <= value <= 30

# Иерархическая структура для EXIF данных
__dict_mapping = {
    "x:xmpmeta": {
        "rdf:RDF": {
            "rdf:Description": {
                # EXIF данные
                "@exif:ExposureTime": ("shutter-speed", "string", str),
                "@exif:FNumber": ("aperture", "string", str),
                "@exif:ISOSpeedRatings": ("iso", "integer", int),
                "@exif:FocalLength": ("focal-length", "string", str),
                "@exif:DateTimeOriginal": ("date-time", "string", str),
                "@exif:ExposureBiasValue": ("exposure-bias", "string", str),
                "@exif:WhiteBalance": ("white-balance", "integer", int),
                "@exif:MeteringMode": ("metering-mode", "integer", int),
                "@exif:Flash": ("flash", "integer", int),
                
                # TIFF данные
                "@tiff:Make": ("camera-make", "string", str),
                "@tiff:Model": ("camera-model", "string", str),
                "@tiff:ImageWidth": ("image-width", "integer", int),
                "@tiff:ImageLength": ("image-height", "integer", int),
                "@tiff:Orientation": ("orientation", "integer", int),
            },
        },
    },
} 