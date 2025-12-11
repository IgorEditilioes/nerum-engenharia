from django.core.mail import send_mail
from django.template.loader import render_to_string


def enviar_emails_orcamento(nome, email_cliente, telefone, mensagem):
    """
    Envia dois e-mails:
    1. Para você (notificação de orçamento)
    2. Para o cliente (confirmação)
    """

    # -----------------------------------
    # 1️⃣ Email para você
    # -----------------------------------
    email_para_voce = render_to_string('email_templates/email_para_voce.txt', {
        'nome': nome,
        'email_cliente': email_cliente,
        'telefone': telefone,
        'mensagem': mensagem,
    })

    send_mail(
        subject=f"Novo orçamento enviado por {nome}",
        message=email_para_voce,
        from_email=None,  # usa DEFAULT_FROM_EMAIL
        recipient_list=['igorediti@gmail.com'], 
    )

    # -----------------------------------
    # 2️⃣ Email para o cliente
    # -----------------------------------
    email_para_cliente = render_to_string('email_templates/email_para_cliente.txt', {
        'nome': nome,
        'telefone': telefone,
        'mensagem': mensagem,
    })

    send_mail(
        subject="Recebemos sua solicitação de orçamento",
        message=email_para_cliente,
        from_email=None,
        recipient_list=[email_cliente],
    )
