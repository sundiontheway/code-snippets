# coding: utf-8
import settings
from model import DatabaseObj
from custom import custom_rules


DB_SRC = DatabaseObj(settings.DB_SRC)
DB_DST = DatabaseObj(settings.DB_DST)

def migrate():
    counter = 0
    finished = True
    while True:
        r = None
        try:
            r = DB_SRC.read()
            if not r:
                print "Read failed %s counter=%s" % (r, counter)
                break
        except StopIteration:
            break
        except Exception, e:
            print str(e)
            finished = False
            break

        try:
            ok = DB_DST.write(custom_rules(r))
            if not ok:
                print "Write failed result=%s!" % r
                finished = False
                break
        except Exception, e:
            print str(e)
            finished = False
            break

        counter += 1

    print "%d data have been Finished. finished=%s" % (counter, finished)
    return finished


if __name__ == "__main__":
    r = migrate()
