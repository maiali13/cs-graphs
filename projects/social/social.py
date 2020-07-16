import sys
import random, math

sys.path.append('../graph')
from util import Queue

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        self.friendships_counter = 0

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)
            self.friendships_counter += 1

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
       # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}

        # Add users
        for i in range(num_users):
            self.add_user(f"User {i}")
        
        # all possible friendship combos
        possible_friendships = []

        # check that last number is larger than 1st number to avoid duplicates
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friendships.append((user_id, friend_id))
        
        # Shuffle the possible friendships
        random.shuffle(possible_friendships)

        # Add friendships
        # we need to divide by 2 since each add_friendship() creates 2 friendships
        for i in range(num_users * avg_friendships // 2):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])
    
    def populate_graph_linear(self, num_users, avg_friendships):
        """
        Stretch: refactor populate_graph to run in O(n) time
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
       
        # add users
        for i in range(num_users):
            self.add_user(f"User {i+1}")  

        # get target number of friendships
        target_friendships = (num_users * avg_friendships)

        # set counters for friendships and collisions
        total_friendships = 0
        collisions = 0

        # while total friendhips < target
        while total_friendships < target_friendships:
            # set user id and friend id to a random int between 1 and number of users
            user_id = random.randint(1, num_users)
            friend_id = random.randint(1, num_users)

            # if return of add friendship for user and friend ids = true,
            if self.add_friendship(user_id, friend_id):
                # increment friendship counter
                total_friendships += 2
            # otherwise increment collision counter
            else:
                collisions += 1
        # print("Total Frienships: {total_friendships} \nTotal Collisions: {collisions}")


    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.

        BFS for shotest path
        """
        visited = {}  # Note that this is a dictionary, not a set
        
        # if no user ID found
        if user_id not in self.users:
            print('WARNING: User id does not exist')
            return
        
        # instantiate queue and enqueue new user id as a list
        q = Queue()
        q.enqueue([user_id])

        # iterate thru friends/neighbors breadth-first
        # while queue is not empty
        while q.size() > 0:
            
            # deueue to path variable
            path = q.dequeue()

            # set user as last item in the path
            user = path[-1]

            # if user is not in visited
            if user not in visited:
                # set user path in visited
                visited[user] = path

            for friend in self.friendships[user]:
                # if neighbor not in visited
                if friend not in visited:
                    # add friend to queue and update path
                    q.enqueue(path + [friend])

        return visited


if __name__ == '__main__':
    print('Social graph of 10 users with 2 friends on average:\n')
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)

    print('\nGenerating a social graph of 100 users with 10 friends on average:\n')
    sg = SocialGraph()
    sg.populate_graph(100, 10)
    friends = 0
    for i in range(1, 100):
        friends += len(sg.friendships[i])
    print('Average Number of friends: ', friends / 100)
    print('Number of times add_friendship() was called', sg.friendships_counter, '\n')

    print('\nGenerating a social graph of 1000 users with 5 friends on average:\n')
    sg = SocialGraph()
    sg.populate_graph(1000, 5)
    extended = 0
    for i in sg.get_all_social_paths(random.randint(1, 1000)).items():
        if len(i[1]) > 2:
            extended += 1
    print('Percent of users in extend social network: ', extended / 1000)