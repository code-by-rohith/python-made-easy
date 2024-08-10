import csv
from pathlib import Path

def main():
    print("Script Started")
    data = []
    with open('test.csv') as csv_file_output:
        csv_reader = csv.reader(csv_file_output)
        count = 0
        for row in csv_reader:
            print(row)
            if count == 0:
               row.append('Final Amount')
               row.append("Discount")
            else:
                  amount = int(row[2])
                  qty = int(row[3])
                  gst = int(row[4])
                  final_amount = amount * qty
                  gst_amount = final_amount * (gst/100)
                  final_total = final_amount + gst_amount
                  offer=final_total*0.5
                  row.append(final_total)
                  row.append(offer)

            count = count + 1
            data.append(row)
            print(data)

        myfile = Path('output.csv')
        with open(myfile, 'w') as csv_file_output:
            writer = csv.writer(csv_file_output)
            for each in data:
                writer.writerow(each)

        print("Script Completed")


main()