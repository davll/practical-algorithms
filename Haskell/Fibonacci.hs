module Fibonacci where

import Control.Monad.State

{- Version 0: Pattern Matching -}

fib_0 :: Int -> Int
fib_0 0 = 0
fib_0 1 = 1
fib_0 n = fib_0 (n-1) + fib_0 (n-2)

{- Version 1: Tail Recursive -}

fib_1 n = go n (0, 1)where
    go n (a, b)  | n == 0         = a
                 | otherwise      = go (n-1) (b, a+b)

{- Version 2: Monadic -}

fib_2 n = flip evalState (0, 1) $ do
    forM [0..(n-1)] $ \_ -> do
        (a,b) <- get
        put (b, a+b)
    (a,b) <- get
    return a

{-  -}
