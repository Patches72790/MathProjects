import pandas

def main():
    df = pandas.read_csv('./data.csv')

    df['midpoint'] = None
    df['weighted_freq'] = None

    for idx, i in enumerate(df['Age']):
        [low, high] = i.split("-")
        print(low, high)
        df['midpoint'][idx] = (int(low) + int(high)) / 2


    for idx, i in enumerate(df['midpoint']):
        df['weighted_freq'][idx] = i * df['Frequency'][idx]
    
    print(df['weighted_freq'].sum() / df['Frequency'].sum())

    print(df)

if __name__ == "__main__":
    main()
