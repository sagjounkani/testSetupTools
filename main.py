import argparse
from Levenshtein import distance as levenshtein_distance


def getData():
    parser = argparse.ArgumentParser(description="Run test")
    parser.add_argument('--input_file', required=True)
    parser.add_argument('--output_file', required=True)
    args = parser.parse_args()
    obj = Distance(args.input_file, args.output_file)
    obj.getDistance()


class Distance:
    def __init__(self, ipFile, opFile):
        self.ipFile = ipFile
        self.opFile = opFile
        self.distance = -1

    def getDistance(self):
        with open(self.ipFile) as f:
            lines = f.readlines()
            self.distance = levenshtein_distance(lines[0], lines[1])

        fout = open(f'{self.opFile}', 'w')
        fout.write(f"{str(self.distance)}")
        fout.close()


if __name__ == "__main__":
    getData()
