{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPvQcZ2XiKmy+2K8sgvuzlU",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/5cxgp59c4b-glitch/stock-analysis/blob/main/%E6%A0%AA%E4%BE%A1%E5%88%86%E6%9E%90.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "b9y2B23BuMI4"
      },
      "outputs": [],
      "source": [
        "import pandas as pd\n",
        "import matplotlib.pyplot as plt\n",
        "from sklearn.linear_model import LinearRegression\n",
        "\n",
        "# データ取得\n",
        "df = pd.read_excel(\"stock-sevenelven.xlsx\")\n",
        "df.columns = df.columns.str.strip()\n",
        "df['date'] = pd.to_datetime(df['date'])\n",
        "\n",
        "# 出来高の棒グラフと終値の折れ線グラフ\n",
        "fig, ax1 = plt.subplots()\n",
        "\n",
        "y1 = df['fixed-finish']\n",
        "x1 = df['date']\n",
        "y2 = df['volume']\n",
        "\n",
        "ax1.plot(x1, y1, label='finish-price')\n",
        "ax1.set_ylabel('Price')\n",
        "\n",
        "ax2 = ax1.twinx()\n",
        "ax2.bar(x1, y2, alpha=0.3, label='Volume')\n",
        "ax2.set_ylabel('Volume')\n",
        "\n",
        "plt.title('Stock Price and Volume')\n",
        "plt.show()\n",
        "\n",
        "# （変化率にすることで、時間におけるトレンドをある程度除去でき）\n",
        "df['return'] = df['fixed-finish'].pct_change()\n",
        "df['volume_change'] = df['volume'].pct_change()\n",
        "df2 = df[['volume_change', 'return']].dropna()\n",
        "x3=df2[['volume_change']]\n",
        "y3=df2[['return']]\n",
        "\n",
        "# 相関係数\n",
        "print(df[['return', 'volume_change']].corr())\n",
        "\n",
        "# 単回帰分析\n",
        "model_lr = LinearRegression()\n",
        "model_lr.fit(x3, y3)\n",
        "\n",
        "plt.plot(x3, y3, 'o')\n",
        "plt.plot(x3, model_lr.predict(x3), linestyle=\"solid\")\n",
        "plt.xlabel('Volume Change')\n",
        "plt.ylabel('Return')\n",
        "plt.show()\n",
        "print(\"係数:\", model_lr.coef_)\n",
        "print(\"切片:\", model_lr.intercept_)\n",
        "print(\"R^2:\", model_lr.score(x3, y3))\n",
        "\n",
        "\n",
        "# ラグありで分析\n",
        "\n",
        "\n",
        "df['volume_lag'] = df['volume_change'].shift(1)\n",
        "df3 = df[['volume_lag', 'return']].dropna()\n",
        "x4 = df3[['volume_lag']]\n",
        "y4 = df3[['return']]\n",
        "# 相関係数（ラグあり）\n",
        "print(df[['return', 'volume_lag']].corr())\n",
        "\n",
        "model_lr2 = LinearRegression()\n",
        "model_lr2.fit(x4, y4)\n",
        "\n",
        "plt.plot(x4, y4, 'o')\n",
        "plt.plot(x4, model_lr2.predict(x4), linestyle=\"solid\")\n",
        "plt.xlabel('Volume Change Lag')\n",
        "plt.ylabel('Return')\n",
        "plt.show()\n",
        "print(\"係数:\", model_lr2.coef_)\n",
        "print(\"切片:\", model_lr2.intercept_)\n",
        "print(\"R^2:\", model_lr2.score(x4, y4))\n"
      ]
    }
  ]
}