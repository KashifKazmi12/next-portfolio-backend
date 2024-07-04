from django.core.exceptions import ValidationError


def validate_video(value):
    valid_extensions = ['.mp4', '.avi', '.mov', '.wmv', '.flv', '.mkv', '.webm']
    if not value.name.lower().endswith(tuple(valid_extensions)):
        raise ValidationError("Only video files (MP4, AVI, MOV, WMV, FLV, MKV, WEBM) are allowed.")