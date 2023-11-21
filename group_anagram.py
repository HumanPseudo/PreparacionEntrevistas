"""
/*
 * Un anagrama es una palabra creada a partir de la reordenación de las letras de otra palabra. Ej: saco - caso
 * Dado un array de strings, devuelve los anagramas agrupados. Cualquier orden es válido.
 *
 * Ejemplo:
 *  Input: words = ["saco", "arresto", "programa", "rastreo", "caso"].
 *  Output: [["saco", "caso"], ["arresto", "rastreo"], ["programa"]].
 */

 """
from collections import defaultdict
from typing import Dict, List
from mypy_extensions import TypedDict

class GroupAnagram:

    def __init__(self):
        pass

    @staticmethod
    def group_anagrams(strs):
        """
        Group anagrams from a list of strings.
        
        Args:
            strs (List[str]): A list of strings to group anagrams from.
        
        Returns:
            List[List[str]]: A list of lists, each containing a group of anagrams.
        """
        anagram_map = defaultdict(list)

        for word in strs:
            # Ordena las letras de la palabra para obtener la clave
            key = "".join(sorted(word))
            anagram_map[key].append(word)

        # Retorna la lista de grupos de anagramas
        return [anagram_group for anagram_group in anagram_map.values()]

    @staticmethod
    def get_anagram_hash(s: str) -> str:
        """
        Calculates the hash of an anagram string.

        Args:
            s (str): The input string.

        Returns:
            str: The hash value of the anagram string.
        """
        letter_count = [0] * 26

        for c in s:
            letter_count[ord(c) - ord('a')] += 1

        return str(letter_count)

    @staticmethod
    def build_anagram_map(strs: List[str]) -> Dict[str, List[str]]:
        """
        Builds a dictionary mapping anagrams to a list of words.
        
        Parameters:
            strs (List[str]): A list of strings representing words.
        
        Returns:
            Dict[str, List[str]]: A dictionary where the keys are anagrams and the values are lists of words that are anagrams of each other.
        """
        anagram_map: Dict[str, List[str]] = defaultdict(list)

        for s in strs:
            hash_key = GroupAnagram.get_anagram_hash(s)
            anagram_map[hash_key].append(s)

        return dict(anagram_map)



