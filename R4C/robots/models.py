from django.db import models


class RobotModel(models.Model):
    model = models.SlugField(
        verbose_name="model",
        help_text="Robot model",
        max_length=2,
        unique=True,
    )

    class Meta:
        verbose_name = "Robot Model"
        verbose_name_plural = "Robot Models"
        ordering = ("-pk",)

    def __str__(self):
        return f"{self.model}"


class RobotVersion(models.Model):
    model = models.ForeignKey(
        RobotModel,
        on_delete=models.CASCADE,
        related_name="versions",
        verbose_name="model",
        help_text="Robot model",
    )
    version = models.SlugField(
        verbose_name="version",
        help_text="Robot model version",
        max_length=2,
    )

    class Meta:
        verbose_name = "Robot Version"
        verbose_name_plural = "Robot Versions"
        ordering = ("-pk",)
        constraints = (
            models.UniqueConstraint(
                fields=("model", "version"),
                name="model_version_unique_constraint",
            ),
        )

    def __str__(self):
        return "-".join((self.model.model, self.version))


class Robot(models.Model):
    version = models.ForeignKey(
        RobotVersion,
        on_delete=models.CASCADE,
        related_name="robots",
        verbose_name="version",
        help_text="Robot's version",
    )
    created = models.DateTimeField(
        verbose_name="created",
        help_text="Robot creation date and time",
    )

    class Meta:
        verbose_name = "Robot"
        verbose_name_plural = "Robots"
        ordering = ("-pk",)

    def __str__(self):
        return f"{self.version}"

    @property
    def serial(self):
        return self.pk

    @property
    def model(self):
        return self.version.model.model
