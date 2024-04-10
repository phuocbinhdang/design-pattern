from abc import ABC, abstractmethod


class Device(ABC):
    @abstractmethod
    def turn_on(self):
        raise NotImplementedError()

    def turn_off(self):
        raise NotImplementedError()


class TV(Device):
    def turn_on(self):
        print("TV is on")

    def turn_off(self):
        print("TV is off")

    def change_channel(self):
        print("TV change channel")


class Stereo(Device):
    def turn_on(self):
        print("Sterio is on")

    def turn_off(self):
        print("Sterio is off")

    def adjust_volumn(self):
        print("Sterio adjust volumn")


class Command(ABC):
    @abstractmethod
    def execute(self):
        raise NotImplementedError()


class TurnOnCommand(Command):
    _device: Device

    def __init__(self, device: Device):
        self._device = device

    def execute(self):
        self._device.turn_on()


class TurnOffommand(Command):
    _device: Device

    def __init__(self, device):
        self._device = device

    def execute(self):
        self._device.turn_off()


class ChangeChannelCommand(Command):
    _tv: TV

    def __init__(self, tv: TV):
        self._tv = tv

    def execute(self):
        self._tv.change_channel()


class AdjustVolumnCommand(Command):
    _stereo: Stereo

    def __init__(self, stereo: Stereo):
        self._stereo = stereo

    def execute(self):
        self._stereo.adjust_volumn()


class Remote:
    _command: Command

    def set_command(self, command: Command):
        self._command = command

    def press_button(self):
        self._command.execute()


if __name__ == "__main__":
    tv = TV()
    stereo = Stereo()

    turn_on_tv_command = TurnOnCommand(tv)
    turn_off_tv_command = TurnOnCommand(tv)
    change_channel_command = ChangeChannelCommand(tv)
    adjust_volumn_stereo_command = AdjustVolumnCommand(stereo)

    remote = Remote()

    remote.set_command(turn_on_tv_command)
    remote.press_button()

    remote.set_command(turn_off_tv_command)
    remote.press_button()

    remote.set_command(change_channel_command)
    remote.press_button()

    remote.set_command(adjust_volumn_stereo_command)
    remote.press_button()
