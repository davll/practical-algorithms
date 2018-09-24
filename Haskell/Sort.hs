module Sort where

mergesort'splitinhalf :: [a] -> ([a], [a])
mergesort'splitinhalf [] = ([], [])
mergesort'splitinhalf xs = (take n xs, drop n xs)
    where
        n = (length xs) `div` 2

mergesort'merge :: (Ord a) => [a] -> [a] -> [a]
mergesort'merge [] xs = xs
mergesort'merge xs [] = xs
mergesort'merge (x:xs) (y:ys)
    | (x < y) = x : mergesort'merge xs (y:ys)
    | otherwise = y : mergesort'merge (x:xs) ys

mergesort :: (Ord a) => [a] -> [a]
mergesort [] = []
mergesort [x] = [x]
mergesort xs = mergesort'merge (mergesort ls) (mergesort rs)
    where (ls, rs) = mergesort'splitinhalf xs

bubblesort'iter :: (Ord a) => [a] -> [a]
bubblesort'iter (x:y:xs)
    | x > y = y : bubblesort'iter (x:xs)
    | otherwise = x : bubblesort'iter (y:xs)
bubblesort'iter (x) = (x)

bubblesort' :: (Ord a) => [a] -> Int -> [a]
bubblesort' xs i
    | i == (length xs) = xs
    | otherwise = bubblesort' (bubblesort'iter xs) (i+1)

bubblesort :: (Ord a) => [a] -> [a]
bubblesort xs = bubblesort' xs 0

quicksort :: (Ord a) => [a] -> [a]
quicksort [] = []
quicksort (x:xs) = quicksort ls ++ [x] ++ quicksort gs
    where
        ls = [y | y <- xs, y <= x]
        gs = [y | y <- xs, y > x]
