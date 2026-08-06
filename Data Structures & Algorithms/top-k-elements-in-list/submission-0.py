class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count how many times each number appears.
        # counter is a dict: number -> frequency
        counter = {}
        for n in nums:
            counter[n] = counter.get(n, 0) + 1

        # counter.items() is iterable - it gives us tuples like (number, frequency).
        # sorted() sorts those tuples, but key=lambda item: item[1] tells it to
        # compare based on the frequency (second element of the tuple) instead
        # of comparing the whole tuple.
        # reverse=True sorts from largest frequency to smallest.
        # [:k] keeps only the first k tuples, which are the k most frequent.
        top_k_entries = sorted(counter.items(), key=lambda item: item[1], reverse=True)[:k]

        # Each entry looks like (number, frequency).
        # We only want the number, so grab entry[0].
        result = []
        for entry in top_k_entries:
            result.append(entry[0])

        return result