from spiders.airbnb import Airbnb

if __name__ == '__main__':
    spider = Airbnb()
    spider.start_requests()