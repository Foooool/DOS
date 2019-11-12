"""
程序主入口
"""

from argparse import ArgumentParser

def main():
    # 解析命令行参数
    arg_parser = ArgumentParser('Distributed Optimization Simulator',
                                usage='Discover new words from corpus according to term frequency, aggreagation coefficient, min neighboring entropy and max neighboring entropy.')

    arg_parser.add_argument('input_path',
                            help='The path to the corpus. It should be a plain text file or a dir containing only plain text files.')
    arg_parser.add_argument('output_path', help='The path to generate the reports.')
    arg_parser.add_argument('--dictionary_path', default=os.path.join(os.path.dirname(jieba.__file__), 'dict.txt'),
                            help='The path to the dictionary (text), each line of which contains item, POS-tag and frequency, seperated by spaces. Terms satisfying the filter condition but in the dictionary are not considered as new words.')
    arg_parser.add_argument('--latin', nargs=4, default=default_latin, type=int,
                            help='The parameters include term frequency, aggreagation coefficient, max neighboring entropy and min neighboring entropy, which also applies for --bigram, --unigram_2 and --unigram_3. This argument set thresholds for latin words, including pure digits, pure letters and the combination of letters and digits such as "iphone 7".')
    arg_parser.add_argument('--bigram', nargs=4, default=default_bigram, type=float,
                            help='Bigrams are defined as words that are composed of two unigram terms. Reference argument --latin for further help.')
    arg_parser.add_argument('--unigram_2', nargs=4, default=default_unigram2, type=float,
                            help='A term which is composed of two Chinese characters and cannot be divided into other words. Reference argument --latin for further help.')
    arg_parser.add_argument('--unigram_3', nargs=4, default=default_unigram3, type=float,
                            help='A term which is composed of three Chinese characters and cannot be divided into other words. Reference argument --latin for further help.')
    arg_parser.add_argument('--iteration', default=default_iteration, type=float,
                            help='The next iteration will base its dictionary as the original dictionary plusing the new words discovered in the last iteration.')
    arg_parser.add_argument('--verbose', default=default_verbose, choices=[0, 1, 2], type=int,
                            help="Determines the verbosity of the reports. *** 0: only new word items and their term frequency.*** 1: min neighboring entropy and max neighboring entropy are supplemented. *** 2:left and right neighboring entropy are added.")
    args = arg_parser.parse_args()


if __name__ == '__main__':
    main()
