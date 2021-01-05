from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Cliente(models.Model):

    YES_ANSWER = "Si"
    NO_ANSWER = "No"
    YES_OR_NO = [
    (YES_ANSWER, 'Si'),
    (NO_ANSWER, 'No'),
    ]

    edades = []
    for i in range(100):
        tup = (str(i), str(i))
        edades.append(tup)

    name = models.CharField(max_length=30)

    edad = models.CharField(
    max_length = 2,
    choices = edades,
    default = "0",
    )

    domicilio = models.CharField(max_length=100, blank=True)
    tel = models.CharField(max_length=15, blank=True)
    mailE = models.CharField(max_length=50, blank=True)

    #first round
    asolea = models.CharField(
    max_length = 2,
    choices = YES_OR_NO,
    default = NO_ANSWER,
    )
    alimenticio = models.CharField(
    max_length = 2,
    choices = YES_OR_NO,
    default = NO_ANSWER,
    )
    embarazada = models.CharField(
    max_length = 2,
    choices = YES_OR_NO,
    default = NO_ANSWER,
    )
    dispositivo = models.CharField(
    max_length = 2,
    choices = YES_OR_NO,
    default = NO_ANSWER,
    )
    menopausia = models.CharField(
    max_length = 2,
    choices = YES_OR_NO,
    default = NO_ANSWER,
    )

    #second round
    cardiacos = models.CharField(
    max_length = 2,
    choices = YES_OR_NO,
    default = NO_ANSWER,
    )
    contacto = models.CharField(
    max_length = 2,
    choices = YES_OR_NO,
    default = NO_ANSWER,
    )
    pdormir = models.CharField(
    max_length = 2,
    choices = YES_OR_NO,
    default = NO_ANSWER,
    )

    #third round
    piel = models.CharField(
    max_length = 2,
    choices = YES_OR_NO,
    default = NO_ANSWER,
    )
    piel_explique = models.TextField(blank=True)

    alergico = models.CharField(
    max_length = 2,
    choices = YES_OR_NO,
    default = NO_ANSWER,
    )
    alergico_explique = models.TextField(blank=True)

    cancer = models.CharField(
    max_length = 2,
    choices = YES_OR_NO,
    default = NO_ANSWER,
    )
    cancer_explique = models.TextField(blank=True)

    cirugia = models.CharField(
    max_length = 2,
    choices = YES_OR_NO,
    default = NO_ANSWER,
    )
    cirugia_explique = models.TextField(blank=True)

    medicamiento = models.CharField(
    max_length = 2,
    choices = YES_OR_NO,
    default = NO_ANSWER,
    )
    medicamiento_explique = models.TextField(blank=True)

    retin = models.CharField(
    max_length = 2,
    choices = YES_OR_NO,
    default = NO_ANSWER,
    )
    retin_explique = models.TextField(blank=True)

    reacutane = models.CharField(
    max_length = 2,
    choices = YES_OR_NO,
    default = NO_ANSWER,
    )
    reacutane_explique = models.TextField(blank=True)

    exfoliantes = models.CharField(
    max_length = 2,
    choices = YES_OR_NO,
    default = NO_ANSWER,
    )
    exfoliantes_explique = models.TextField(blank=True)

    ahas = models.CharField(
    max_length = 2,
    choices = YES_OR_NO,
    default = NO_ANSWER,
    )
    elAhas_explique = models.TextField(blank=True)

    peeling = models.CharField(
    max_length = 2,
    choices = YES_OR_NO,
    default = NO_ANSWER,
    )
    peeling_explique = models.TextField(blank=True)

    alcohol = models.CharField(
    max_length = 2,
    choices = YES_OR_NO,
    default = NO_ANSWER,
    )
    alcohol_explique = models.TextField(blank=True)
    alcohol_cuanto = models.TextField(blank=True)

    #round 4
    cara = models.TextField(blank=True)

    caseros = models.CharField(
    max_length = 2,
    choices = YES_OR_NO,
    default = NO_ANSWER,
    )
    ardor = models.CharField(
    max_length = 2,
    choices = YES_OR_NO,
    default = NO_ANSWER,
    )
    faciales = models.CharField(
    max_length = 2,
    choices = YES_OR_NO,
    default = NO_ANSWER,
    )

    #round 5
    expuesto = models.CharField(
    max_length = 2,
    choices = YES_OR_NO,
    default = NO_ANSWER,
    )
    expuesto_explique = models.TextField(blank=True)

    bcontrol = models.CharField(
    max_length = 2,
    choices = YES_OR_NO,
    default = NO_ANSWER,
    )
    bcontrol_explique = models.TextField(blank=True)

    #round 5
    epilepsia = models.CharField(
    max_length = 2,
    choices = YES_OR_NO,
    default = NO_ANSWER,
    )
    claustrofobia = models.CharField(
    max_length = 2,
    choices = YES_OR_NO,
    default = NO_ANSWER,
    )
    hemofilia = models.CharField(
    max_length = 2,
    choices = YES_OR_NO,
    default = NO_ANSWER,
    )
    diabetes = models.CharField(
    max_length = 2,
    choices = YES_OR_NO,
    default = NO_ANSWER,
    )
    hepatitis = models.CharField(
    max_length = 2,
    choices = YES_OR_NO,
    default = NO_ANSWER,
    )
    varices = models.CharField(
    max_length = 2,
    choices = YES_OR_NO,
    default = NO_ANSWER,
    )
    fuma = models.CharField(
    max_length = 2,
    choices = YES_OR_NO,
    default = NO_ANSWER,
    )

    otro1 = models.TextField(blank=True)

    pasos = models.CharField(
    max_length = 2,
    choices = YES_OR_NO,
    default = NO_ANSWER,
    )
    placa = models.CharField(
    max_length = 2,
    choices = YES_OR_NO,
    default = NO_ANSWER,
    )
    clavos = models.CharField(
    max_length = 2,
    choices = YES_OR_NO,
    default = NO_ANSWER,
    )
    implantes = models.CharField(
    max_length = 2,
    choices = YES_OR_NO,
    default = NO_ANSWER,
    )
    sinusitis = models.CharField(
    max_length = 2,
    choices = YES_OR_NO,
    default = NO_ANSWER,
    )
    migrana = models.CharField(
    max_length = 2,
    choices = YES_OR_NO,
    default = NO_ANSWER,
    )
    otro2 = models.TextField(blank=True)



    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('client-detail', kwargs={'pk': self.pk})
