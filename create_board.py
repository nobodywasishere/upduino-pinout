#!/usr/bin/env python

# For reference
# Created by Xark
"""
                 PCF  Pin#  _____  Pin#  PCF
                      ------| USB |------
                <GND> |  1   \___/   48 | spi_ssn   (16)
                <VIO> |  2           47 | spi_sck   (15)
                <RST> |  3           46 | spi_mosi  (17)
               <DONE> |  4           45 | spi_miso  (14)
     <RGB2>   led_red |  5           44 | gpio_20   <N/A w/OSC, G3>
     <RGB0> led_green |  6     U     43 | gpio_10   <input-only>
     <RGB1>  led_blue |  7     P     42 | <GND>
                <+5V> |  8     D     41 | <12 MHz>
              <+3.3V> |  9     U     40 | gpio_12
                <GND> | 10     I     39 | gpio_21
              gpio_23 | 11     N     38 | gpio_13
              gpio_25 | 12     O     37 | gpio_19
              gpio_26 | 13           36 | gpio_18
              gpio_27 | 14     V     35 | gpio_11
              gpio_32 | 15     3     34 | gpio_9
<output-only> gpio_35 | 16     .     33 | gpio_6
              gpio_31 | 17     0     32 | gpio_44   <G6>
     <G1>     gpio_37 | 18           31 | gpio_4
     <G0>     gpio_34 | 19           30 | gpio_3
              gpio_43 | 20           29 | gpio_48
              gpio_36 | 21           28 | gpio_45
              gpio_42 | 22           27 | gpio_47
              gpio_38 | 23           26 | gpio_46
              gpio_28 | 24           25 | gpio_24
                      -------------------
        (Assumes OSC jumper shorted and gpio_20 for clock)
"""
# https://pinout.readthedocs.io/en/latest/tutorial.html

from pinout import diagram

pinout_diagram = diagram.Diagram()

pinout_diagram.add_image(0, -2, 260, 718, 'board_260x718.svg', embed=True)
pinout_diagram.add_stylesheet('board_diagram.css', embed=True)

diagram.Label.default_width = 110
diagram.Label.default_height = 25
diagram.Label.default_gap = 6
diagram.Label.default_cnr = 3

label_categories = [
    # (name, tag(s)),
    ('Power', 'pwr'),
    ('GND', 'gnd'),
    # ('gpio', 'gpio'),
    ('DPIO', 'dpio'),
    ('LED', 'led'),
    ('UART', 'serial'),
    ('SPI', 'spi'),
    ('I3C', 'i3c'),
    ('Global input', 'gbin'),
    ('Oscillator', 'osc'),
]

pinout_diagram.add_legend(570, 190, 200, 'legend legend-labels', label_categories)

pin_headers = [
    {
        # LHS header - lower half
        'pin_coords': (23, 15),
        'label_coords': (-50, 15),
        'pitch': 30,
        'labels': [
            [('GND', 'gnd')],
            [('VIO', 'pwr')],
            [('RST', 'gpio')],
            [('DONE', 'gpio')],
            [('41','gpio'),('RGB2 RED', 'led')],
            [('39','gpio'),('RGB0 GRE', 'led')],
            [('40','gpio'),('RGB1 BLU', 'led')],
            [('5v', 'pwr')],
            [('3.3v', 'pwr')],
            [('GND', 'gnd')],
            [('23', 'gpio'),('I3C', 'i3c')],
            [('25', 'gpio'),('I3C', 'i3c')],
            [('26', 'gpio'),('(T 27)', 'dpio')],
            [('27', 'gpio'),('(C 26)', 'dpio')],
            [('32', 'gpio'),('(T 31)', 'dpio')],
            [('35', 'gpio'),('G0','gbin')],
            [('31', 'gpio'),('(C 32)', 'dpio')],
            [('37', 'gpio'),('(T 34)', 'dpio'),('G1','gbin')],
            [('34', 'gpio'),('(C 37)', 'dpio')],
            [('43', 'gpio'),('(T 36)', 'dpio')],
            [('36', 'gpio'),('(C 43)', 'dpio')],
            [('42', 'gpio'),('(T 38)', 'dpio')],
            [('38', 'gpio'),('(C 42)', 'dpio')],
            [('28', 'gpio')],
        ]
    },{
        # RHS header
        'pin_coords': (233, 15),
        'label_coords': (300, 15),
        'pitch': 30,
        'labels': [
            [('16','gpio'),('SSN', 'spi')],
            [('15','gpio'),('SCK', 'spi'),('USB RX','serial')],
            [('17','gpio'),('MOSI', 'spi')],
            [('14','gpio'),('MISO', 'spi'),('USB TX','serial')],
            [('20','gpio'),('(C 13)', 'dpio'),('G3','gbin')],
            [('10','gpio')],
            [('GND','gnd')],
            [('12MHz','osc')],
            [('12', 'gpio'),('(T 21)', 'dpio')],
            [('21', 'gpio'),('(C 12)', 'dpio')],
            [('13', 'gpio'),('(T 20)', 'dpio')],
            [('19', 'gpio')],
            [('18', 'gpio')],
            [('11', 'gpio')],
            [('9', 'gpio')],
            [('6', 'gpio')],
            [('44', 'gpio'),('(C 47)', 'dpio'),('G6','gbin')],
            [(' 4', 'gpio'),('(T  3)', 'dpio')],
            [(' 3', 'gpio'),('(C  4)', 'dpio')],
            [('48', 'gpio'),('(T 45)', 'dpio')],
            [('45', 'gpio'),('(C 58)', 'dpio')],
            [('47', 'gpio'),('(T 44)', 'dpio')],
            [('46', 'gpio')],
            [('2', 'gpio')],
        ]
    },{
        # Lower header - remaining 3 pins
        'pin_coords': (166, 695),
        'label_coords': (300, 750),
        'pitch': 30,
        'labels': [
            [('GND', 'gnd')],
            [('5v', 'pwr')],
        ]
    }
]

for header in pin_headers:
    pinout_diagram.add_pin_header(header)

pinout_diagram.export('board_diagram.svg', overwrite=True)
