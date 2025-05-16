{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "43236899-8ae1-4de8-a858-7bd4904475c0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "11250\n"
     ]
    }
   ],
   "source": [
    "def main():\n",
    "    import sys\n",
    "\n",
    "    # Simulated standard input for Jupyter\n",
    "    input_text = \"\"\"2\n",
    "4\n",
    "3 -1 1 10\n",
    "5\n",
    "9 -5 -5 -10 10\"\"\"\n",
    "    input_lines = input_text.strip().splitlines()\n",
    "\n",
    "    def process_tests(lines, idx, acc):\n",
    "        if idx >= len(lines):\n",
    "            return acc\n",
    "\n",
    "        x_line = lines[idx].strip()\n",
    "        nums_line = lines[idx + 1].strip() if idx + 1 < len(lines) else ''\n",
    "        \n",
    "        try:\n",
    "            x = int(x_line)\n",
    "            nums = list(map(int, nums_line.split()))\n",
    "            if len(nums) != x:\n",
    "                return process_tests(lines, idx + 2, acc + ['-1'])\n",
    "            else:\n",
    "                def process_yn(yns, i, total):\n",
    "                    if i >= len(yns):\n",
    "                        return total\n",
    "                    if yns[i] <= 0:\n",
    "                        return process_yn(yns, i + 1, total + yns[i] ** 4)\n",
    "                    return process_yn(yns, i + 1, total)\n",
    "                total = process_yn(nums, 0, 0)\n",
    "                return process_tests(lines, idx + 2, acc + [str(total)])\n",
    "        except:\n",
    "            return process_tests(lines, idx + 2, acc + ['-1'])\n",
    "\n",
    "    try:\n",
    "        n = int(input_lines[0].strip())\n",
    "        results = process_tests(input_lines[1:], 0, [])\n",
    "        def print_lines(lst, i):\n",
    "            if i >= len(lst):\n",
    "                return\n",
    "            print(lst[i])\n",
    "            print_lines(lst, i + 1)\n",
    "        print_lines(results, 0)\n",
    "    except:\n",
    "        pass\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    main()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9f06ddb7-141d-4e8e-97e6-ebc8cd378310",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
