import sys, time
import prettytable as pt

# tb = pt.PrettyTable()
# tb.field_names = ["项目","进度","百分比"]

for i in range(10):
    # tb.add_row(["新闻", ("=" * i) + ">", str(i * 100 / 10) + "%"])
    sys.stdout.write("\r{0}>".format("="*i))
    sys.stdout.flush()
    time.sleep(0.5)
    # tb.clear_rows
# print(tb)