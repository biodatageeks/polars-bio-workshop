import polars_bio as pb

pb.set_option("datafusion.execution.target_partitions", "4")
bgz_path = "../data/gencode.v49.annotation.gff3.bgz"
df = pb.scan_gff(bgz_path, projection_pushdown=True,
                 parallel=True).select(["chrom", "start", "end"])
df2 = df
pb.overlap(df, df2, low_memory=True).sink_parquet("/tmp/test.parquet")