"""Package of utility functions for lists."""
type EmbeddedList = list[int | EmbeddedList]

def list_flattener( data: EmbeddedList) -> list[int]:
    """Recursively flattens an arbitrarily nested list of integers.
    Args: 
        data: nested list of integers

    Returns:
        A list of intergers generated from the input list.
    """

    flattened: list[int] = []

    for item in data:
        if isinstance(item, int):
            flattened.append(item)
        else:
            new_items = list_flattener(item)
            flattened.extend(new_items)

    return flattened
