"""Sakai top calculator"""

import math
import logging


logging.basicConfig(level=logging.INFO, format='%(message)s')


BEND_NUM = 4  # Do not change!
CIRCLE = 360.0  # Never change!!!
ANGLE = 53.7  # Ideal Sakai cut angle


def calculate(length, bend_radius, tip, handle):
    """Calculate Sakai top

    Args:
        length (float): length of the paper clip's wire in mm
        bend_radius (float): radius of bend (depends of the wire calibre)
        tip (float): tip length
        handle (float): handle length
    """
    # Decrease a length of wire with tip and handle lengths
    rest = length - tip - handle - bend_radius * BEND_NUM
    logging.info(f'Rest: {rest:.2f}')

    # Calculate a needed part of wire for circle
    circle_length_coeff = (CIRCLE - ANGLE) / CIRCLE
    logging.info(f'Circle lenght coeff: {circle_length_coeff:.2f}')

    # Radius of the top
    # l = 2 * R + k * 2 * R * pi
    radius = rest / (2 * (1 + circle_length_coeff * math.pi))
    logging.info(f'Radius: {radius:.2f}')

    # Segment (top circle with a cut) length
    segment = rest - 2 * radius
    logging.info(f'Segment: {segment:.2f}')

    # Check
    logging.info(f'Check: length = {length:.2f}, sum = {tip + bend_radius + radius + bend_radius + segment + bend_radius + radius + bend_radius + handle:.2f}')

    logging.info((
        f'Bend every (mm):\t{tip}\t{bend_radius}\t'
        f'{radius:.1f}\t{bend_radius}\t'
        f'{segment:.1f}\t{bend_radius}\t'
        f'{radius:.1f}\t{bend_radius}\t'
        f'{handle}'
        ))


if __name__ == '__main__':
    length = 174.0
    bend_radius = 1.0
    tip = 6.0
    handle = 12.0

    calculate(length, bend_radius, tip, handle)
