from typing import List, Dict, Any


def flatten_list(nested_list: List[List[Any]]) -> List[Any]:
    """
    Flattens a nested list.
    
    Args:
        nested_list (List[List[Any]]): A list of lists to flatten.
    
    Returns:
        List[Any]: A flat list containing all elements from the nested lists.
    """
    return [item for sublist in nested_list for item in sublist]


def merge_dicts(dicts: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Merges multiple dictionaries into one.
    
    Args:
        dicts (List[Dict[str, Any]]): A list of dictionaries to merge.
    
    Returns:
        Dict[str, Any]: A single dictionary containing merged key-value pairs.
    """
    merged = {}
    for d in dicts:
        merged.update(d)
    return merged


def calculate_average(numbers: List[float]) -> float:
    """
    Calculates the average of a list of numbers.
    
    Args:
        numbers (List[float]): A list of numbers to average.
    
    Returns:
        float: The average of the numbers. Returns 0 if the list is empty.
    """
    return sum(numbers) / len(numbers) if numbers else 0.0
