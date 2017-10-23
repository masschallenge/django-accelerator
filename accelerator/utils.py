from django.core.validators import RegexValidator


def url_validator():
    schema = "^[hH][tT][tT][pP][sS]?://"
    netloc_element = "([^/:@]+(:[^/@]+)?@)?([\w-]+)"
    dot = "\."

    url_regex = "{schema}({netloc_element}{dot})+{netloc_element}".format(
        schema=schema,
        netloc_element=netloc_element,
        dot=dot
    )

    return RegexValidator(
        regex=url_regex,
        message="Enter a valid URL")
