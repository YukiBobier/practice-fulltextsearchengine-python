from __future__ import annotations

import collections
import MeCab


def createSimplestEngine() -> Engine:
    return Engine()


class Engine:
    def __init__(self) -> None:
        self._documents: dict[int, str] = {}
        self._next_document_id: int = 1
        self._index: dict[int, collections.Counter] = {}
        self._tagger = MeCab.Tagger()

    def save(self, document: str) -> None:
        # Update the documents.
        document_id = self._next_document_id
        self._documents[document_id] = document
        self._next_document_id += 1

        # Update the index.
        node = self._tagger.parseToNode(document)
        while node:
            token = node.feature.split(",")[10]
            postings = self._index.setdefault(token, collections.Counter())
            postings.update([document_id])

            node = node.next

    def search(self, term: str) -> list[tuple[int, str]]:
        # Make the term to tokens.
        node = self._tagger.parseToNode(term)
        tokens = []
        while node:
            token = node.feature.split(",")[10]
            tokens.append(token)

            node = node.next

        # Look up the index and aggregate the frequency.
        intersection = self._index.get(token[0], collections.Counter())
        aggregated = self._index.get(token[0], collections.Counter())
        for token in tokens[1:]:
            postings = self._index.get(token, collections.Counter())
            intersection = intersection & postings
            aggregated = aggregated + postings

        # Sort the results in order of their frequency.
        return sorted(
            [
                (document_id, self._documents[document_id])
                for document_id in intersection
            ],
            key=lambda d: aggregated[d[0]],
            reverse=True,
        )
