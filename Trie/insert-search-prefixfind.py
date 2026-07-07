# question
# =====================
# Implement a Trie (prefix tree) with three operations:
#   - insert(word)      : insert a word into the trie
#   - search(word)      : return True if the exact word exists
#   - prefixFind(prefix): return True if any inserted word starts with prefix
#
# Approach:
#   - Each TrieNode holds a children dict (char → TrieNode) and an is_word_end flag.
#   - insert: walk each character, create a node if missing, mark is_word_end at the last char.
#   - search: walk each character, return False if any char is missing,
#             return is_word_end at the last node (True only if full word was inserted).
#   - prefixFind: same walk as search but return True once all prefix chars are found —
#                 doesn't check is_word_end since we only need a matching prefix, not a full word.
#
# Note: search vs prefixFind — "app" inserted, search("ap") = False, prefixFind("ap") = True.
#   The is_word_end flag is what distinguishes a full word from a prefix.

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_word_end = True
        return self.root

    def search(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        if node.is_word_end:
            return True
        return False

    def prefixFind(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True


# test
# ============
# search(word)       → True only if exact word was inserted
# prefixFind(prefix) → True if any inserted word starts with prefix

trie = Trie()
for word in ["apple", "app", "application", "apt", "bat", "ball"]:
    trie.insert(word)

test_cases = [
    # (method, arg, expected, desc)

    # search — exact word match
    ("search",     "apple",       True,  "exact word inserted"),
    ("search",     "app",         True,  "shorter word also inserted"),
    ("search",     "ap",          False, "prefix only, not a full word"),
    ("search",     "application", True,  "longer word inserted"),
    ("search",     "apply",       False, "word not inserted"),
    ("search",     "bat",         True,  "different root word"),
    ("search",     "ba",          False, "prefix of 'bat', not inserted as word"),
    ("search",     "cat",         False, "entirely absent word"),
    ("search",     "",            False, "empty string — root has no is_word_end"),

    # prefixFind — any inserted word starts with prefix
    ("prefixFind", "ap",          True,  "prefix shared by apple/app/apt"),
    ("prefixFind", "app",         True,  "prefix of apple/app/application"),
    ("prefixFind", "appl",        True,  "prefix of apple/application"),
    ("prefixFind", "apple",       True,  "full word is also a valid prefix"),
    ("prefixFind", "apples",      False, "extends beyond any inserted word"),
    ("prefixFind", "ba",          True,  "prefix of bat/ball"),
    ("prefixFind", "ball",        True,  "full word as prefix"),
    ("prefixFind", "cat",         False, "no word starts with this prefix"),
    ("prefixFind", "",            True,  "empty prefix matches everything"),
]

passed = 0
for idx, (method, arg, expected, desc) in enumerate(test_cases, 1):
    result = getattr(trie, method)(arg)
    ok = result == expected
    passed += ok
    status = "PASS" if ok else "FAIL"
    print(f"Test {idx:2}: {status}  {method}({arg!r:15}) — {desc}")
    if not ok:
        print(f"         result:   {result}")
        print(f"         expected: {expected}")

print(f"\n{passed}/{len(test_cases)} tests passed")
