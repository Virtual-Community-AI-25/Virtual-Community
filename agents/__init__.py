from .agent import Agent, AgentLogger, AgentProcess

def get_agent_cls(agent_type, robot_type=None):
    if agent_type == 'tour_agent':
        if robot_type is None:
            from .tour_agent import TourAgent
            return TourAgent
        elif robot_type == 'go2':
            from .go2_agent import Go2TourAgent
            return Go2TourAgent
        elif robot_type == 'h1':
            from .h1_agent import H1TourAgent
            return H1TourAgent
        elif robot_type == 'google_robot':
            from .google_robot_agent import GoogleRobotTourAgent
            return GoogleRobotTourAgent
        elif robot_type == 'husky':
            from .husky_agent import HuskyTourAgent
            return HuskyTourAgent
        elif robot_type == 'drone':
            from .drone_agent import DroneTourAgent
            return DroneTourAgent
        else:
            raise NotImplementedError
    else:
        raise NotImplementedError
