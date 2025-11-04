EOF = "EOF"  # sentinel symbol

class TwoBuffer:
    def __init__(self, text, buffer_size=5):
        self.text = text
        self.buffer_size = buffer_size
        self.buffers = [[], []]  # two buffers
        self.pos = 0             # position in text
        self.active = 0          # active buffer index
        self.forward = 0         # pointer in buffer

        # Load first buffer
        self.load_buffer(0)

    def load_buffer(self, idx):
        start = self.pos
        end = min(self.pos + self.buffer_size, len(self.text))
        self.buffers[idx] = list(self.text[start:end]) + [EOF]
        self.pos = end
        print(f"Buffer[{idx}] loaded: {self.buffers[idx]}")

    def get_next_char(self):
        char = self.buffers[self.active][self.forward]
        self.forward += 1

        if char == EOF:
            if self.pos < len(self.text):
                # Switch buffer
                self.active = 1 - self.active
                self.forward = 0
                self.load_buffer(self.active)
                return self.get_next_char()  # recursive call
            else:
                return None  # True EOF
        else:
            return char

# ----------------------
# Example Usage
# ----------------------
text = "hello world!"
scanner = TwoBuffer(text, buffer_size=5)

print("Characters read using Two-Buffer:\n")
while True:
    ch = scanner.get_next_char()
    if ch is None:
        print("\n[END] All characters processed.")
        break
    print(f"Read: {ch}")
