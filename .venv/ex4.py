def build_xml_element(tag, content, **attributes):
    # Start the opening tag
    element = f"<{tag}"

    # Add each attribute to the opening tag
    for attr, value in attributes.items():
        element += f' {attr}="{value}"'

    # Add the content and close the tag
    element += f">{content}</{tag}>"

    return element


# Example usage
result = build_xml_element(
    "a", "Hello there", href="http://python.org", _class="my-link", id="someid"
)
print(result)  # Output: <a href="http://python.org" _class="my-link" id="someid">Hello there</a>
