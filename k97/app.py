import reflex as rx

class State(rx.State):
    faturamento_dia: float = 0.0

def index():
    return rx.vstack(
        rx.heading("K97 TERMINAL", color="#10b981"),
        rx.text(f"Faturamento: R$ {State.faturamento_dia}", font_size="2em"),
        rx.button("GERAR COBRANÇA PIX", color_scheme="emerald"),
        padding="2em",
        bg="#020617",
        height="100vh",
        align_items="center",
    )

app = rx.App()
app.add_page(index)
