2023-11-12

- Bug fixes / improvements:
  - GEOSUnaryUnion: Fix crash on collection containing empty point (GH-830, Dan Baston)
  - IndexedFacetDistance: Fix crash with Inf coordinates (GH-821, Dan Baston)
  - HausdorffDistance: Fix crash on collection containing empty point (GH-840, Dan Baston)
  - MaximumInscribedCircle: Fix infinite loop with non-finite coordinates (GH-843, Dan Baston)
  - DistanceOp: Fix crash on collection containing empty point (GH-842, Dan Baston)
  - GEOSClipByRect: Fix case with POINT EMPTY (GH-913, Mike Taves)
  - Remove undefined behaviour in use of null PrecisionModel (GH-931, Jeff Walton)
  - Skip over testing empty distances for mixed collections (GH-979, Paul Ramsey)
  - Add missing cstdint headers (GH-990, GH-743, Regina Obe, Sergei Trofimovich)


