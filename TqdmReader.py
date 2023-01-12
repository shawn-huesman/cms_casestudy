from tqdm import tqdm


class TqdmReader:
    def __init__(self, resp):
        total_size = int(resp.headers.get("Content-Length", 0))

        self.resp = resp
        self.bar = tqdm(
            desc=resp.url,
            total=total_size,
            unit="iB",
            unit_scale=True,
            unit_divisor=1024,
        )

        self.reader = self.read_from_stream()

    def read_from_stream(self):
        for line in self.resp.iter_lines():
            line += b"\n"
            self.bar.update(len(line))
            yield line

    def read(self, n=0):
        try:
            return next(self.reader)
        except StopIteration:
            return ""
