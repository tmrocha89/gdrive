import sys
import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler




class MyHandler (PatternMatchingEventHandler):
    patterns = ["*"]
    #print event.src_path, event.event_type
    def on_modified(self, event):
        #self.process(event)
        print "estou no modificado"

    def on_created(self, event):
        #self.process(event)
        print "estou no criado"

    def on_moved(self, event):
        #self.process(event)
        print "estou no modificado"

    def on_created(self, event):
        #self.process(event)
        print "estou no criado"



path = "/media/work/Development/Python/gdrive/dir/"

observer = Observer()
observer.schedule(MyHandler(), path, recursive=True)
observer.start()
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()