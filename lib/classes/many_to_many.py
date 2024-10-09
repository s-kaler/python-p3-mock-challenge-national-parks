from typing import Any


class NationalPark:
    all = []

    def __init__(self, name):
        if not isinstance(name, str) or len(name) <= 3:
            raise Exception('Name must be a string longer than 3 characters') 
        self.name = name
        NationalPark.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if hasattr(self, '_name'):
            print('Cannot change name after initialization')
        else:
            self._name = name
        
    def trips(self):
        trips = []
        for trip in Trip.all:
            if trip.national_park == self:
                trips.append(trip)
        return trips
    
    def visitors(self):
        visitors = []
        for trip in Trip.all:
            if trip.national_park == self:
                if trip.visitor not in visitors:
                    visitors.append(trip.visitor)
        return visitors
            
    
    def total_visits(self):
        visits = 0
        for trip in Trip.all:
            if trip.national_park == self:
                visits += 1
        return visits
    
    def best_visitor(self):
        if self.total_visits() == 0:
            return None
        most_visited_visitor = None
        max_visits = 0
        for visitor in self.visitors():
            visits = 0
            for trip in Trip.all:
                if trip.visitor == visitor:
                    visits += 1
            if visits > max_visits:
                max_visits = visits
                most_visited_visitor = visitor
        return most_visited_visitor



class Trip:
    all = []

    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        if not isinstance(start_date, str) or len(start_date.split(' ')) != 2:
            raise Exception('Start date must be a string of Month Day format')
        self._start_date = start_date
        if not isinstance(end_date, str) or len(end_date.split(' ')) != 2:
            raise Exception('End date must be a string of Month Day format')
        self.end_date = end_date
        Trip.all.append(self)

    @property
    def start_date(self):
        return self._start_date
    
    @start_date.setter
    def start_date(self, start_date):
        if not isinstance(start_date, str) or len(start_date.split(' ')) != 2:
            raise Exception('End date must be a string of Month Day format')
        self._start_date = start_date

    @property
    def end_date(self):
        return self._end_date
    
    @end_date.setter
    def end_date(self, end_date):
        if not isinstance(end_date, str) or len(end_date.split(' ')) != 2:
            raise Exception('End date must be a string of Month Day format')
        self._end_date = end_date

class Visitor:
    all = []

    def __init__(self, name):
        if not isinstance(name, str) or not (len(name) >= 1 and len(name) <= 15):
            raise Exception('Name must be a string between 1 and 15 characters')
        self.name = name
        Visitor.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not isinstance(name, str) or not (len(name) >= 1 and len(name) <= 15):
            raise Exception('Name must be a string between 1 and 15 characters')
        self._name = name
        
    def trips(self):
        trips = []
        for trip in Trip.all:
            if trip.visitor == self:
                trips.append(trip)
        return trips
    
    def national_parks(self):
        parks = []
        for trip in self.trips():
            if trip.national_park not in parks:
                parks.append(trip.national_park)
        return parks
    
    def total_visits_at_park(self, park):
        visits = 0
        for trip in self.trips():
            if trip.national_park == park:
                visits += 1
        return visits