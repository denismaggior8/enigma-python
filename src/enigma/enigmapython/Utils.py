
class Utils:


    @staticmethod
    def find_divergence(str1, str2):
        """
        Finds the index where two strings first diverge, 
        and the characters at that index in both strings.
        
        Args:
            str1 (str): The first string.
            str2 (str): The second string.
        
        Returns:
            tuple: (index, char1, char2) where index is the position of divergence,
                char1 is the character in str1 at the divergence,
                and char2 is the character in str2 at the divergence.
                If the strings only diverge in length, char1 and char2 will be None.
                If the strings are identical, returns None.
        """
        # Iterate through both strings up to the length of the shorter string
        for i in range(min(len(str1), len(str2))):
            if str1[i] != str2[i]:
                return i, str1[i], str2[i]  # Return the index and differing characters
        
        # If the strings differ in length
        if len(str1) != len(str2):
            return min(len(str1), len(str2)), None, None
        
        # If the strings are identical
        return None

    @staticmethod
    def find_all_subclasses(cls):
        return set(cls.__subclasses__()).union(
            [s for c in cls.__subclasses__() for s in Utils.find_all_subclasses(c)])

    @staticmethod    
    def swap_chars(string, ch1, ch2):
        if ch1 == ch2: return string
        str_list = []
        for char in string:
            if char == ch1:
                str_list.append(ch2)
            elif char == ch2:
                str_list.append(ch1)
            else:
                str_list.append(char)
        return ''.join(str_list)
    