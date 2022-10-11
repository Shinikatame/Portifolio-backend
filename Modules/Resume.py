from fpdf import FPDF

class Resume(FPDF):
    def __init__(self, data: dict):
        super().__init__()
        self.index = 0
        self.data = data

    def header(self):
        self.set_margin(10)
        
        self.set_fill_color(0, 0, 128)
        self.rect(0, 0, 250, 50, 'F')

        self.set_text_color(240, 248, 255)
        self.set_font('helvetica', 'BI', 20)
        
        self.cell(txt = self.data['name'])
        self.ln(7)

        self.flex(self.data['profession'], self.data['state'])
        self.flex(self.data['email'], self.data['phone'])

        github, linkedin = self.data["social"]
        self.flex(f'{github["name"]}: {github["username"]}', f'{linkedin["name"]}: {linkedin["username"]}', github["url"], linkedin['url'])

        self.set_text_color(0, 0, 0)
        self.ln(10)

    def about(self):
        self.ln(10)

        self.set_margin(20)
        self.set_font('helvetica', 'B', 15)
        self.multi_cell(0, txt = self.data['about'])

        self.set_margin(10)

    def topic(self, title: str):
        self.ln(10)
        self.index = 0

        self.set_font('helvetica', 'BU', 20)
        self.cell(0, txt = title, align = 'C')

        self.ln(10)

    def topicItem(self, item: str):
        if self.index == 0:
            self.index += 1
            align = 'L'
            self.ln(10)

        elif self.index == 1:
            self.index += 1
            align = 'C'

        else:
            align = 'R'
            self.index = 0

        self.set_right_margin(13)
        self.set_left_margin(13)

        self.set_font('helvetica', '', 15)
        self.cell(62, txt = item, align = align)

        self.set_left_margin(10)
        self.set_right_margin(10)

    def subtopic(self, subtitle: str):
        self.ln(10)
        self.index = 0

        self.set_left_margin(15)
        self.set_font('helvetica', 'B', 15)
        self.cell(0, txt = f'- {subtitle}')

        self.ln(4)
        self.set_left_margin(10)

    def subtopicItem(self, item: str):
        if self.index == 0:
            self.index += 1
            align = 'L'
            self.ln(5)

        elif self.index == 1:
            self.index += 1
            align = 'C'

        else:
            align = 'R'
            self.index = 0

        self.set_right_margin(23)
        self.set_left_margin(23)

        self.set_font('helvetica', 'I', 15)
        self.cell(50, txt = item, align = align)

        self.set_left_margin(10)
        self.set_right_margin(10)

    def flex(self, textL: str, textR: str, linkL: str = None, linkR: str = None):
        self.ln(7)

        self.set_font('helvetica', 'BU', 12) if linkL else self.set_font('helvetica', 'B', 12)
        self.cell(95, txt = textL, link = linkL, align = 'l')

        self.set_font('helvetica', 'BU', 12) if linkR else self.set_font('helvetica', 'B', 12)
        self.cell(95, txt = textR, link = linkR, align = 'r')

        self.set_font('helvetica', size = 10)

