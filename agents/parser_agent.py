class ParserAgent:
    def parse(self, raw_data):
        return {"status": "parsed", "features": ["log", "config", "command_output"]}