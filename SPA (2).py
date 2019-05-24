import sys
import scipy.spatial as euclid


class SPA(object):
    """
    """
    def __init__(self):
        self.p_max = 147
        self.d_max = 500

    def location_of_stops(self, choice, distance):
        """
        Min(WD) = Sigma[D(ij)*X(ij)]
        X(ij)=1 for all i in P
        D(ij) is the matrix that represents the Eucledian Distance between user i in P and stop j in n
        distance = [100, 200, 300, 150, 250, 350, 400, 450, 500]
        """
        avg_dist = 0
        min_dist = 1000
        max_dist = 0

        if choice == 1:
            #for dist_ in distance:
            #    if int(dist_) < min_dist:
            #        min_dist = dist_
            return min(distance)
        elif choice == 2:
            for dist_ in distance:
                if int(dist_) > max_dist:
                    max_dist = dist_
            return max_dist
        elif choice == 3:
            for dist_ in distance:
                avg_dist += int(dist_)
            return avg_dist/9
        else:
            print "Wrong Choice"
            return None


    def _calculate_euclidean_distance(self, inp):
        """
        Eucledian_Distance = {||u-v||}^2
        """
        euclid_dist = []
        for items in inp:
            user_i, stop_j = items.split(' ')
            euclid_dist.append(euclid.distance.euclidean(user_i, stop_j))
        return euclid_dist

    def definition_of_services(self):
        """
        max(balance) = Sigma[Z(ik)*Tariff_fixed] + Sigma[Z(ik)*Tariff_variable*D(vij)*Speed(vij)]
                        - Sigma[B(ijk)*D(ij)*Cost*Speed(ij)]
        """
        return True


    def system_fleet_dimensioning(self):
        """
        Max(Operational Profit) = [D(i)*Sigma{Tariff_fixed+{Tariff_km*Dist(Ai1Ai2)} + Tariff_time*{Time(i2)-Time(i1)}]
                        - Sigma[{1-Sigma[M(ij)]}*Costf[ceiling(D(i)/8)] + Sigma[Dist(Ai1Ai2)+Sigma[Dist(ij)*M(ij) * Costv[ceiling(Di/8)]]

        Sigma[M(ij)] <= 1
        Time(ji) >= (Time(i2) + TT(ij)) * M(ij) - l * (1-M(ij))
        D(ij) - vector that defines the numbers of customer assigned to service i belongs to A
        Time(ik) - vector that defines the departure and arrival time of service i belongs to A(where K=1 for departure
                    time and and K=1 for arrival time
        TT(ij) - matrix that represents the travel time estimates during the peak traffic hour from node i to node j,
                where i, j belongs to N
        DIST(ij) - matrix that represents the road network distance from node i to node j (EucledianDistance*Sinousityindex)
        Cost(f) - fixed cost of operation of the Minibus of capacity b belongs to B
        Cost(v) - variable cost of each kilometre travelled by each Minibus of capacity b belongs to B
        Constants:
        t(max)  - Maximum waiting time
        Tariff_fixed - Fixed component of the ticket price charged to the passengers between a singel trip
        Tariff_km - Variable fee charged to the user by kilometre travelled
        Tariff_time - Variable fee charged to the user by travel time
        """




if __name__ == "__main__":
    sp = SPA()
    inp = []
    #distance = [100, 200, 300, 150, 250, 350, 400, 450, 500]
    #print "Enter 9 pairs of User and Stop. Both the values should be separated by a single space and an" \
    #      " enter between each such pair"
    print "Enter 9 euclidean distances"
    for i in xrange(9):
        inp.append(raw_input())
    #distance = sp._calculate_euclidean_distance(inp)
    distance = inp

    print "To find out the:\n" \
          "1.Average Distance - Enter 3\n" \
          "2.Minimum Distance - Enter 1\n" \
          "3.Maximum Distance - Enter 2\n"
    inp = int(raw_input())
    result = sp.location_of_stops(choice=inp, distance=distance)
    print "The answer for your choice is {a} metres".format(a=result)


